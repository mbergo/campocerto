# Atualizar a lista de pacotes disponíveis
sudo apt update

# Instalar o pip
sudo apt install python3-pip

# Instalar as dependências do Flask
pip3 install flask
pip3 install mysql-connector-python

# Instalar o framework Bootstrap
sudo apt install npm
sudo npm install -g bootstrap

# Instalar o gerenciador de pacotes bower
sudo npm install -g bower

# Baixar o Bootstrap com o bower
bower install bootstrap

# Criar a pasta 'static' na raiz da aplicação
mkdir static

# Mover o Bootstrap para a pasta 'static'
mv bower_components/bootstrap/dist/* static/
