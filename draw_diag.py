from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('string', 'string_manipulator.py')
cfg.build_visual('string', 'png')