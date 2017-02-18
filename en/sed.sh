sed -i 's/`\\(/\$/g' content/*
sed -i 's/\\)`/\$/g' content/*
sed -i 's/\\\[$/\$\$/g' content/*
sed -i 's/\\\[/\$\$/g' content/*
# sed -i 's/^.* \\\]/\$\$/g' content/*
sed -i 's/\\\]/\$\$/g' content/*
