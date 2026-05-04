from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required  # 추가됨
from .utils import load_assets, get_asset_by_id
from .models import Post

def asset_list(request):
    """금융 자산 리스트 (JSON에서 로드)"""
    assets = load_assets()
    context = {"assets": assets}
    return render(request, "community/asset_list.html", context)


def board(request, asset_id):
    """해당 자산의 토론 게시판 (게시글 목록)"""
    asset = get_asset_by_id(asset_id)
    if not asset:
        return render(request, "community/404.html", status=404)
    posts = Post.objects.filter(asset_id=asset_id)
    context = {"asset": asset, "posts": posts}
    return render(request, "community/board.html", context)


def post_detail(request, asset_id, post_id):
    """게시글 상세"""
    asset = get_asset_by_id(asset_id)
    if not asset:
        return render(request, "community/404.html", status=404)
    post = get_object_or_404(Post, id=post_id, asset_id=asset_id)
    context = {"asset": asset, "post": post}
    return render(request, "community/post_detail.html", context)


@login_required  # 로그인 사용자만 접근 가능 (비로그인 시 로그인 페이지로 리다이렉트)
@require_http_methods(["GET", "POST"])
def post_create(request, asset_id):
    """게시글 작성"""
    asset = get_asset_by_id(asset_id)

    if not asset:
        return render(request, "community/404.html", status=404)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title and content:
            Post.objects.create(
                asset_id=asset_id,
                title=title,
                content=content,
                author=request.user.username,  # 폼 입력이 아닌 로그인된 사용자의 username 자동 저장
            )
            return redirect("community:board", asset_id=asset_id)
            
    context = {"asset": asset}
    return render(request, "community/post_form.html", context)


@login_required  # 로그인 사용자만 접근 가능
@require_http_methods(["GET", "POST"])
def post_update(request, asset_id, post_id):
    """게시글 수정"""
    asset = get_asset_by_id(asset_id)

    if not asset:
        return render(request, "community/404.html", status=404)
        
    post = get_object_or_404(Post, id=post_id, asset_id=asset_id)

    # 본인 글이 아니면 수정 차단 및 오류 메시지 출력
    if post.author != request.user.username:
        messages.error(request, "본인이 작성한 글만 수정할 수 있습니다.")
        return redirect("community:post_detail", asset_id=asset_id, post_id=post.id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        
        if title and content:
            post.title = title
            post.content = content
            # author는 변경하지 않음
            post.save()
            return redirect("community:post_detail", asset_id=asset_id, post_id=post.id)

    context = {
        "asset": asset,
        "post": post,
        "title": post.title,
        "content": post.content,
        "is_edit": True,
    }
    return render(request, "community/post_form.html", context)


@login_required  # 로그인 사용자만 접근 가능
@require_http_methods(["POST"])
def post_delete(request, asset_id, post_id):
    """게시글 삭제"""
    post = get_object_or_404(Post, id=post_id, asset_id=asset_id)
    
    # 본인 글이 아니면 삭제 차단 및 오류 메시지 출력
    if post.author != request.user.username:
        messages.error(request, "본인이 작성한 글만 삭제할 수 있습니다.")
        return redirect("community:post_detail", asset_id=asset_id, post_id=post.id)

    post.delete()
    messages.success(request, "게시글이 삭제되었습니다.")
    return redirect("community:board", asset_id=asset_id)