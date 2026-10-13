# 해외 물류 · 사업 대시보드

팀이 함께 보는 수입·수출 프로젝트 / WBS 대시보드입니다.

## 파일
- `index.html` — 대시보드 (브라우저로 열기)
- `data.json` — 모든 내용(프로젝트, 필수정보, 공유사항, WBS)
- `images/` — 제품 이미지 (예: `images/pour.jpg` → 프로젝트 수정에서 경로 입력)
- `index.template.html`, `build.py` — data.json을 index.html에 내장할 때 사용 (`python3 build.py`)

## 함께 쓰는 방법
1. 저장소 Settings → Pages → Branch `main` / root 로 켜면 팀원 모두 같은 주소로 봅니다.
2. 대시보드에서 프로젝트 추가·수정, 체크, 공유사항 등록 → 내 브라우저에 임시 저장됩니다.
3. 상단 **data.json 내보내기** → 받은 파일을 저장소의 `data.json`에 덮어써 커밋(깃허브 웹에서 Add file → Upload files).
4. 다른 팀원은 새로고침하면 반영됩니다. (본인이 수정 중인 내용이 있으면 노란 안내가 뜨고, "서버 버전으로 되돌리기"로 최신본을 받을 수 있습니다.)

> 두 사람이 동시에 수정하면 나중에 올린 data.json이 덮어씁니다. 올리기 전 새로고침으로 최신본을 받은 뒤 수정하세요.
