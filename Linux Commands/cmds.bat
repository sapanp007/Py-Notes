::cat survey_results_schema.csv

awk -F',' '{print $4,$5}' survey_results_schema.csv

awk -F',' '{if($1 ~ "Age") print $1,"--",$2}' survey_results_schema.csv
awk -F',' '{if($1 ~ /Age/) print $1,"--",$2}' survey_results_schema.csv

::sed --> permanent

sed 's/old/new/g' survey_results_schema.csv
sed '2,5 s/old/new/g' survey_results_schema.csv
sed 's/old/new/7' survey_results_schema.csv


sed '/pattern/d' survey_results_schema.csv
sed '1,3d' survey_results_schema.csv
sed '1,$d' survey_results_schema.csv

cat survey_results_schema.csv

::zip
tar -cvzf filename.tar.gz
::unzip
tar -xvzf sample.tar.gz