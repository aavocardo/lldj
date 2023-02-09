conda create --name <name> --file ./init/environment.txt
conda create --name <name> --file environment.txt
conda activate <name>
pip install -r ./init/packages.txt
pip install -r packages.txt
