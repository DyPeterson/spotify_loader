## Database populate

### Contributors:

 

 
- [Dylan Peterson](https://github.com/DyPeterson)

  

### Description

  

A [Data Stack Academy](https://www.datastack.academy/) code review project to create a database and load csvs into the database.

  

### Technologies Used:

- [Python](https://www.python.org/)

- [Pandas](https://pandas.pydata.org/)

- [SQLAlchemy](https://www.sqlalchemy.org/)

- [MariaDb](https://mariadb.org/)

#### Programs used:

  

- [Visual Code Studio](https://code.visualstudio.com/)

  

- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US) ( Running: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) ([ubuntu 20.04](https://releases.ubuntu.com/20.04/)))
- [Beekeeper Studio](https://www.beekeeperstudio.io/)

  
- [Docker](https://www.docker.com/) (Required for scripts to run)
  

### Setup & Installation:

  

1. Through the terminal like [GitBash](https://git-scm.com/downloads)

  
	
	1. Open the terminal and navigate to where you would like the new project to be using `cd` commands. Its also recommended that you make a new directory using `mkdir *directory-name*`.

	  

	1. Clone the repository using the command `git clone https://github.com/DyPeterson/spotify_loader.git`

	  

	1. After cloning the directory it will appear in the directory that your terminal is set to. So make sure you are in the directory that you want this project copied to.

	  

	1. Once this project is cloned you can navigate to that folder within your terminal and create a virtual environment `python3.7 -m venv *any-name*`. Now activate the venv with `source *any-name*/bin/activate`

	  

	1. Install requirements in venv `pip install -r requirements.txt`

	  

	1. Download the data by running the `get_data.sh` either by clicking it or running in the terminal.

	  

	1.  `code .` to open in default coding software.

  

2. Through github.com

  
	
	1. Go to the project's directory page **[HERE](https://github.com/DyPeterson/spotify_loader.git)**

	  

	1. Click the green `code` button to open the drop-down menu.

	  

	1. At the bottom of the menu will have *Download Zip*. Go ahead and click it to download the project.

	  

	1. Once downloaded find the `.zip` file and right-click it to bring up the menu. Within that menu click `Extract Here` to extract it in the current folder or click `Extract Files...`to select which folder you would like the project in.

	  

	1. Once the project has been extracted, locate the folder in a terminal and open it with `code .` .

3.  Once inside the projects repository, run the `spotify_docker.sh` script.
4.  Download CSVs with `gsutil -m cp gs://data.datastack.academy/spotify/spotify_artists.csv gs://data.datastack.academy/spotify/spotify_albums.csv .`command in terminal. Move these files into `./data` directory (create one if non-existent)
5. Run the `main.py`  with the command `python main.py`to populate and transform the database.

### Link to project on GitHub

  

[https://github.com/DyPeterson/spotify_loader.git](https://github.com/DyPeterson/spotify_loader.git)

  
  

### Details


Contact me with any questions or suggestions [Here](dylan.peterson17@gmail.com)

  

### Known Bugs

  

Cannot write tables to db because of *sql error 1054, unknown columns in 'field list'*

  

### Copyright 2022

  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.