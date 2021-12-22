import cProfile, pstats
profiler = cProfile.Profile()
profiler.enable()

...

profiler.disable()
stats = pstats.Stats(profiler).sort_stats('tottime')
stats.print_stats()