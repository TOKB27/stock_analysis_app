# my_project/django/Dockerfile
FROM centos:7

# 必要なパッケージのインストール
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install git gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel patch mariadb-devel python3-devel pkgconfig

# MySQLクライアントのインストール
RUN yum -y install mysql

# Node.jsとnpmのインストール
RUN curl -sL https://rpm.nodesource.com/setup_16.x | bash - && \
    yum -y install nodejs

# pyenvのインストール
RUN curl https://pyenv.run | bash

# 環境変数の設定
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH:/usr/local/bin:/usr/local/lib/node_modules

# Python 3.9.7のインストールと設定
RUN pyenv install 3.9.7
RUN pyenv global 3.9.7

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# requirements.txtのコピー
COPY ./requirements.txt /usr/src/app/

# パッケージのインストール
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# package.jsonとpackage-lock.jsonのコピー
COPY ./package.json ./package-lock.json /usr/src/app/

# Node.jsの依存関係をインストール
RUN npm install

# Tailwind CSSの初期化
RUN npx tailwindcss init

# プロジェクトのコピー
COPY . /usr/src/app/

# Tailwind CSSのビルド
RUN npm run build-css

# ポートの公開
EXPOSE 8000

# サーバーの起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
