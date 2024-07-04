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

```yml
function_name:
  inputs:
    - input_name:
        constraints:
          - constraint_1
          - constraint_2
  # Add other functions similarly
```