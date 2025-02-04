DO $$ 
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'email_db') THEN
        CREATE DATABASE email_db;
    END IF;
END $$;
