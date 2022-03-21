
# **Datatypes** 

## integer 
    10,     
    -10,    
    1578

## float (wip)
    0.123,  
    12.123,     
    -0.000001

## vector (wip)
    {0,1,5.0}   
    {12.123,0.00,150}
    {0,0,0}

## matrix
## string (wip)     


VEX includes a string datatype. This is useful in several places:

- Manipulating text

- Referencing filenames and op: node names

- Manipulating binary data


### string literals
 strings can be enclosed by double "" or single '' quotes.

    'foos'   
    "$HIP/references/img_01.jpg" 

**raw strings vs non-raw strings.**
raw strings ignore escape sequences. "\n" will be interpreted as "\n".
for more escape sequences, go to https://en.cppreference.com/w/cpp/language/escape

non-raw strings will automatically convert escape sequences to their representative byte sequences. "\n" wil convert to the ASCII byte to emit  newline.
you can also escape strings:

## struct
## dictionary
## bsdf

>💡     
> ### scientific notation for small and large numbers:     
>this is the standard form 5,3*10^5
>