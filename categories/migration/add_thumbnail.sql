BEGIN;
ALTER TABLE "categories_category" ADD COLUMN "thumbnail" varchar(100);
COMMIT;
