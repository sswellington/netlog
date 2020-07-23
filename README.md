# Netlog


## Dependency
> Python version 3.8.3
### Virtualenv
~~~bash
# Create virtualenv
python3 -m virtualenv vnetlog \

# Activate virtualenv
cd vnetlog/netlog \
source ../bin/activate
~~~

#### vscode
To select a specific environment, use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P).

Or 

~~~
mkdir .vscode \
cd .vscode \
touch settings.json && echo "
// PS. Replace single quotes to double quotes
{
    'python.pythonPath': '$PATHOFVIRTUALENV/bin/activate'
} " > settings.json 
~~~

[Source](https://code.visualstudio.com/docs/python/environments)

#### import
~~~bash
pip install speedtest-cli
curl -O https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
~~~