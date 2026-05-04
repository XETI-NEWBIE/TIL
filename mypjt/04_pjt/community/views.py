import json
import os
from collections import Counter

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post

ASSET_THEME_MAP = {
    '주식': 'theme-stock',
    '원자재': 'theme-material',
    '채권': 'theme-bond',
    '암호자산': 'theme-crypto',
}

RISK_CLASS_MAP = {
    '하': 'risk-low',
    '중하': 'risk-midlow',
    '중': 'risk-medium',
    '중상': 'risk-midhigh',
    '상': 'risk-high',
}


def decorate_asset(asset):
    enriched = asset.copy()
    enriched['theme_class'] = ASSET_THEME_MAP.get(asset['category'], 'theme-default')
    enriched['risk_class'] = RISK_CLASS_MAP.get(asset['risk_level'], 'risk-medium')
    return enriched


def get_assets():
    path = os.path.join(settings.BASE_DIR, 'data', 'assets.json')
    with open(path, 'r', encoding='utf-8') as file:
        return [decorate_asset(asset) for asset in json.load(file)]


def get_asset(asset_id):
    return next((asset for asset in get_assets() if asset['id'] == asset_id), None)


def render_asset_not_found(request):
    return render(request, 'community/404.html', status=404)


def index(request):
    assets = get_assets()
    risk_counts = Counter(asset['risk_level'] for asset in assets)

    context = {
        'assets': assets,
        'asset_count': len(assets),
        'category_count': len({asset['category'] for asset in assets}),
        'high_risk_count': risk_counts.get('상', 0) + risk_counts.get('중상', 0),
        'stable_asset_count': risk_counts.get('하', 0) + risk_counts.get('중하', 0),
    }
    return render(request, 'community/index.html', context)


def board(request, asset_id):
    asset = get_asset(asset_id)
    if not asset:
        return render_asset_not_found(request)

    posts = Post.objects.filter(asset_id=asset_id).order_by('-created_at')
    context = {
        'asset': asset,
        'posts': posts,
        'post_count': posts.count(),
    }
    return render(request, 'community/board.html', context)


def create(request, asset_id):
    asset = get_asset(asset_id)
    if not asset:
        return render_asset_not_found(request)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.asset_id = asset_id
            post.save()
            return redirect('community:board', asset_id=asset_id)
    else:
        form = PostForm()

    return render(request, 'community/create.html', {'form': form, 'asset': asset})


def detail(request, asset_id, post_id):
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    asset = get_asset(asset_id)
    if not asset:
        return render_asset_not_found(request)

    return render(request, 'community/detail.html', {'post': post, 'asset': asset})


def update(request, asset_id, post_id):
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    asset = get_asset(asset_id)
    if not asset:
        return render_asset_not_found(request)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:detail', asset_id=asset_id, post_id=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'community/update.html',
        {'form': form, 'post': post, 'asset': asset},
    )


def delete(request, asset_id, post_id):
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    if request.method == 'POST':
        post.delete()
        if get_asset(asset_id):
            return redirect('community:board', asset_id=asset_id)
        return redirect('community:index')

    return redirect('community:detail', asset_id=asset_id, post_id=post.pk)
