# skip_magic
IPython / Jupyter skip magic command to control cell execution programmatically

Place on first line of cell to control execution.

  %skip True
  print(42)

skips cell execution.

  %skip $run_flags['steptype'] is False
  print(42)

to evaluate `run_flags` variable as skip condition.

## Improvements

Manage having an other magic command. Case such as:
%%skip $dont_run
%%time
print(42)

## Credits

Initial proposal & code by Robbe
on https://stackoverflow.com/questions/26494747/simple-way-to-choose-which-cells-to-run-in-ipython-notebook-during-run-all
