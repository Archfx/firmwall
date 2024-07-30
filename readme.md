firmwall
---

Multi arch binary analysis tool for ...


### Run instructions

```shell
./run.sh
```

Components

- List functions
- System call Idefication
- Symbolic input preperation for untrusted function calls
- Src to destination symbolic simulation
- Constraint check


### Spec Template

Constraints and the funtion defintions are passed to the Firmwall using simple yml scripts and the templates for the data structures and functions are as below,

__Data structure template__

```yml
  structures:
  - structure:
    name: 
    type: 
    constraints: 
      - constraint_1
      - constraint_2
  # Add other structures similarly
```

__Function defintion template__

```yml
  functions:
  - function:
      name: 
      num_args: 
      arg_i: 
        name:
        type: 
        constraints:
          - constraint1
          - constraint2
      output:
        type:
  # Add other functions similarly
```

Data structures and function defintions have different formats in yml format. Please check the [sample_promt.md](scripts/sample_prompt.md) for more instructions on generating the specification using LLMs.