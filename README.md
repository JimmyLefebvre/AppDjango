## Description
Django database for the mobile application 'appli_recolte_android_v2". 

## Install the  database
Edit the script named buildme_inside.sh to match the folder : 
`apppath=/opt/applirecoltedjango`
Execute the script (you mest be admin of the machine)
create a superuser when asked. 

## Administration of the database
open a navigator and go to http://127.0.0.1:8078/admin/

## Enter a new experiment
You must prepare a csv file containing the following information : 
`code_accession,code_lot_plante,lieu,parcelle,nom_lot,nombre_plante,lot_origine,espece,graine_objectif,remarque`

import this file via the "Plantation" page.
