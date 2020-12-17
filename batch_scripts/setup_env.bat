call cd ..
call conda env create -f environment.yml
call conda activate PowerDict
call ipython kernel install --user --name=PowerDict
pause