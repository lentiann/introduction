#Krijimi i venv ne Python hapat:

1. Python duhet te jete i instaluar varesisht nga version qe nevojitet.
2. python-venv paketa duhet te jete gjithashtu e instaluar.
3. mundemi te perdorim 'package-manager' te ndryshem sikur pip, poetry qe jane me te njohura.

Arsyeja kryesore per perdorim te venv eshte, menagjimi i paketave per produkt specific qe e krijojme, dhe mos te kete 'global' per arsye qe mund te rezultoje ne konflikt te versionit te packages.

python3 -m venv virtualenv_1 ---> venv eshte pacakge qe eshte ne OS dhe na mundeson krijim e env.

Pastaj duhet me e zgjedhe environment siq e demostrova. edhe duhet me mbyll console qe me u hap automatik virtualvenv

Skillsat me te rendesishem jane edhe debugging i kodit qe na mundeson ekzekutm te kodit hap pas hapi. si ne vijim

Per probleme ma komplekse, eshte me i nevojshem sesa kodi aktual eshte i thjeshte shume

F5 -> Zakoisht fillon program ose skripten -> Pastaj perdoret per te vazhdu procesin deri ne breakpoint tjeter nese nuk ka vazhdon deri ne fund te programit
F10 -> perdore per te vazhduar ne rreshtin tjeter te kodit
F11 -> per te u futur brenda funksionit ne nivel me te detajuar.


#Creating the requirements.txt can be done with the following command: pip freeze > requirements.txt
#Krijimi i requirements.txt mund të bëhet me komandën e mëposhtme: pip freeze > requirements.txt