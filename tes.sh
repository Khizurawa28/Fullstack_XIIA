#!/bin/bash

# 1. Buat direktori proyek
mkdir -p ~/devops_workspace/auto_capstone
cd ~/devops_workspace/auto_capstone

# 2. Buat Virtual Environment
py -m venv venv_auto

# 3. Aktifkan venv
source venv_auto/bin/activate

# 4. Buat file requirements.tx
echo "Flask" > requirements.txt
echo "numpy" >> requirements.txt

# 5. Install dependencies
pip install -r requirements.txt

# 6. Uji coba pemanggilan pustaka
if py -c "import flask, numpy; print(f'Flask: {flask._version_}, numpy: {numpy._version_}')"; then
    echo "--------------------------------"
    echp "Status: Virtual Environment Siap Digunakan!" 
    echo "--------------------------------"
else
    echo "Terjadi error pada pemasangan pustaka/module"
fi
