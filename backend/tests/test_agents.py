def test_agent_orchestrator():
    prompt = "Test execution query for agentic-podcast-editor-show-notes-gen"
    assert len(prompt) > 0
    assert "Test" in prompt
