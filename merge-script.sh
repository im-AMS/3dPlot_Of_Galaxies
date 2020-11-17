#! /bin/bash
(

for i in *.csv;do
# delete if there is any line containing #Table in 1st 3 lines 
    sed -i '1,3 {/#/d;}' $i
#     store the index of csv in a var
    index=$(head -n 1 $i)
#     delete all the index of all files
    sed -i '1,3 {/[A-Za-z]/d;}' $i
done


cat *.csv >> merged.csv

sort -u merged.csv -o sorted.csv

rm merged.csv

echo "Almost done!"

for i in  *.csv;do

# paste the index to starting of line
    sed -i  "1 i${index}" $i
done

echo "Done!"

)| pv
