from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.podcast_editor_show_notes_gen.schemas import AgenticPodcastEditorShowNotesGenSessionCreate, AgenticPodcastEditorShowNotesGenSessionResponse
from app.domain.podcast_editor_show_notes_gen.service import AgenticPodcastEditorShowNotesGenService

router = APIRouter(prefix="/api/v1/podcast_editor_show_notes_gen", tags=["Agentic Podcast Editor Show Notes Gen Domain"])

@router.post("/sessions", response_model=AgenticPodcastEditorShowNotesGenSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticPodcastEditorShowNotesGenSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Podcast Editor Show Notes Gen.
    """
    return AgenticPodcastEditorShowNotesGenService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticPodcastEditorShowNotesGenSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticPodcastEditorShowNotesGenService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
