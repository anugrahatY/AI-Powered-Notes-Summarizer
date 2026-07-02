from src.supabase_client import supabase

def save_note(user,result):

    supabase.table("notes").insert({

        "user_id":user.id,

        "filename":result["filename"],

        "storage_path":result["storage_path"],

        "summary":result["summary"]

    }).execute()