call cd ..
call conda env create -f environment.yml
call conda activate PowerDictionary
call ipython kernel install --user --name=PowerDictionary
pause