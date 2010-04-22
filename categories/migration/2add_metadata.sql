BEGIN;
ALTER TABLE "categories_category" ADD COLUMN "alternate_title" varchar(100);
ALTER TABLE "categories_category" ADD COLUMN "meta_keywords" varchar(255);
ALTER TABLE "categories_category" ADD COLUMN "meta_extra" text;
ALTER TABLE "categories_category" ALTER COLUMN "description" TYPE text;
COMMIT;
