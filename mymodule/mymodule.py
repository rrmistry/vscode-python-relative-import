# Testing relative import with IPython Kernel in VS Code

#%% Change working directory from the workspace root to the .py file location.
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'mymodule')) # change directory
    print(os.getcwd())
except:
    pass # ignore error in-case re-running this cell
    # (e.g. new cwd = `Project root/mymodule/mymodule`)

#%%
import os
import sys
import config

#%%
print("Environment Variable DATASETS: " +
    config.config["DATASETS"]
)

#%%
