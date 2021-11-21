cd ../..

# Install python 2

sudo apt-get install python2

# Install pip

sudo apt-get update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py

# Install virtualenv

pip install virtualenv

# Create and activate the virtual env

virtualenv --python=2.7 env
source env/bin/activate

# Install Django in the virtualenv

pip install -r requirements.txt

# Install Jupyterlab to run the notebooks

cd beginningdjango-master/
pip install -r requirements_test.txt
cd 1_introduction_to_django/