BEGIN;
ALTER TABLE "categories_category" ADD COLUMN "description" varchar(255);
COMMIT;