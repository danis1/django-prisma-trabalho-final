from dotenv import load_dotenv 
from supabase import create_client 
import os 

load_dotenv()   

SUPABASE_URL=("https://ktzpqsmrtbkkhmxxptjs.supabase.co")
SUPABASE_KEY=("sb_publishable_pa6S1AcBThLyrEzG-lETjQ_Ee2qBV5B")

if not SUPABASE_URL or not SUPABASE_KEY: 
    raise RuntimeError("Configure SUPABASE_URL e SUPABASE_KEY no arquivo .env") 

supabase = create_client(SUPABASE_URL, SUPABASE_KEY,) 