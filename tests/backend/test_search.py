from app.core.search import SearchEngine

def test_search():
    engine = SearchEngine()
    results = engine.search("test query")
    assert len(results) > 0
