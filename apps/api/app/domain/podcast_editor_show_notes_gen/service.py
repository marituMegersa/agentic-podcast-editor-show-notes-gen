from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.podcast_editor_show_notes_gen.models import AgenticPodcastEditorShowNotesGenSession, AgenticPodcastEditorShowNotesGenItem
from app.domain.podcast_editor_show_notes_gen.schemas import AgenticPodcastEditorShowNotesGenSessionCreate, AgenticPodcastEditorShowNotesGenItemCreate

class AgenticPodcastEditorShowNotesGenService:
    @staticmethod
    def create_session(db: Session, data: AgenticPodcastEditorShowNotesGenSessionCreate) -> AgenticPodcastEditorShowNotesGenSession:
        db_obj = AgenticPodcastEditorShowNotesGenSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticPodcastEditorShowNotesGenSession:
        return db.query(AgenticPodcastEditorShowNotesGenSession).filter(AgenticPodcastEditorShowNotesGenSession.id == session_id).first()
