

docs=txt/*
pattern='participant'
egrep -i -l "$pattern" $docs
