### 개발 환경
- python v3.12.0

### 로컬 설정
1. 현재 디렉터리의 python 버전을 3.12.0 으로 설정
```sh
$ brew install pyenv # python 버전 관리 패키지 설치
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ source ~/.zshrc
$ pyenv install 3.12.0
$ pyenv local 3.12.0
```

2. 가상 환경 구성
```sh
$ cd pipo-backend
$ python -m venv .venv
```