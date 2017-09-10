# Binary Attack folder
We do save scripts and that kind of stuff here because we add the path to the bin folder in our
.zprofile with

``` bash
# Specific path for ~/Attack/bin folder
# this dir exists (or should exist) on every system I own.
if [[ -d ~/Attack/bin && ( -d ~/Attack/bin/Darwin || -d ~/Attack/bin/Linux ) ]]; then
  path=(
    ~/Attack/bin/$(uname -s)
    $path
  )
fi
```

Hope this may help you a bit ;)

