# my_project/django/Dockerfile
FROM centos:7

# 必要なパッケージのインストール
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install git gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel patch mariadb-devel python3-devel pkgconfig

# pyenvのインストール
RUN curl https://pyenv.run | bash

# 環境変数の設定
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Python 3.9.7のインストールと設定
RUN pyenv install 3.9.7
RUN pyenv global 3.9.7

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# requirements.txtのコピー
COPY requirements.txt /usr/src/app/

# パッケージのインストール
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# プロジェクトのコピー
COPY . /usr/src/app

# ポートの公開
EXPOSE 8000

# サーバーの起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
