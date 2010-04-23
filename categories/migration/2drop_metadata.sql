BEGIN;
ALTER TABLE "categories_category" DROP COLUMN "alternate_title" varchar(100);
ALTER TABLE "categories_category" DROP COLUMN "meta_keywords" varchar(255);
ALTER TABLE "categories_category" DROP COLUMN "meta_extra" text;
ALTER TABLE "categories_category" ALTER COLUMN "description" TYPE varchar(255);
COMMIT;
