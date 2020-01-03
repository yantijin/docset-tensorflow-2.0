function getdir(){
	for element in `ls $1`
	do
		dir_or_file=$1"/"$element
		if [ -d $dir_or_file ]
		then 
			getdir $dir_or_file
		else
			if [ "${dir_or_file##*.}"x = "html"x ]
			then 
				echo $dir_or_file
				sed -i 's/.md/.html/g' $dir_or_file
				sed -i 's/\/code\/stable/https:\/\/github.com\/tensorflow\/tensorflow\/blob\/r2.0/g' $dir_or_file
			fi
		fi
	done
}
root_dir="./out"
getdir $root_dir

