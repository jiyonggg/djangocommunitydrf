# 💬 멋사 7주차 과제: DRF로 커뮤니티 구현하기

## ⚙️ 구성
- 사용 프레임워크: Django, Django Rest Framework(DRF)
- 프로젝트 이름: community
- 앱 구성
  - board: 전반적인 게시판

## 🔗 URI
- `/board/`: 전체 게시글 목록 불러오기 (GET)
- `/board/post/create/`: 게시글 작성하기 (POST)
- `/board/post/detail/{post_id}/`: 게시글 상세페이지 불러오기 (GET)
- `/board/post/update/{post_id}/`: 게시글 수정하기 (PUT)
- `/board/post/delete/{post_id}/`: 게시글 삭제하기 (DELETE)
- `/board/comment/create/{post_id}/`: 게시글에 댓글 작성하기 (POST)
- `/board/comment/list/{post_id}/`: 특정 게시글의 댓글 목록 불러오기 (GET)