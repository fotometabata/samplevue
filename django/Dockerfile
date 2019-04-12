FROM python:3.7.2
ENV LANG en_US.utf8
WORKDIR /code
ADD requirements.txt /code
RUN apt-get update
RUN pip install -r requirements.txt
RUN apt-get install -y mysql-client

# nodejsの11.xの最新版をインストール（10.xに変えた場合、10.x最新をインストール）
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

# vue-cli3.x系をインストール（vue initを実行できるようにinitもインストールしておく）
RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-init

# axiosをインストール（ajax通信用ライブラリ）
# front側のプロジェクト作成後に実行する
RUN npm install axios --save
RUN npm install moment --save