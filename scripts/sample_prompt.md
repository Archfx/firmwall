Using the following convention to represent the functions defined in Trusted Firmware-M, convert all the data types defined in PSA Cryptography API.

### Data structure parameter definitions

`name` - name of the data type
`type` - type of the data structure (ex:'uint8_t, int32_t') 
`constraints` - constraints on this data type (ex: min, max values, invalid values)


#### Sample functional specification for the `psa_open_key` in cryptographic service

```yaml
  structures:
  -	structure:
	name: psa_key_id_t
	type: uint32_t
	constraints: [PSA_KEY_ID_USER_MIN<, PSA_KEY_ID_USER_MAX>,  PSA_KEY_ID_VENDOR_MIN<, PSA_KEY_ID_VENDOR_MAX>, !=0]
```

### Function parameter description:

`name` - name of the function 
`num_args` - number of arguments
	`arg_i` - for number of elements in `num_args`,
		`name` - name of the function input
		`type` - type of the input
		`size` - bit size of the input
		`constraints` - constrains on the input
`output` - output of the function


#### Sample functional specification for the `psa_open_key` in cryptographic service

```yaml
  functions:
  - function:
      name: psa_open_key
      num_args: 2
      arg_1: 
        name: id
        type: psa_key_id_t
        constraints: []
      arg_2: 
        name: handle
        type: psa_key_handle_t*
        constraints: []
      output:
        type: psa_status_t
```