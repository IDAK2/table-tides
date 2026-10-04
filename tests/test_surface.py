from pathlib import Path
SOURCE=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text(encoding="utf-8")
def test_surface():
    for name in ["set_table","place_guest","reset_paused_room","get_dinner","get_dinners_page","get_reviews_page","get_summary"]:assert f"def {name}" in SOURCE
def test_consensus_and_guards():
    for term in ["run_nondet_unsafe","guest or chair already placed","conflict_limit","SEATED","PAUSED","access_ok","separation_ok","balance_ok"]:assert term in SOURCE
def test_runner():assert SOURCE.startswith('# { "Depends": "py-genlayer:')
