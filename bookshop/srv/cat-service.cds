using { sap.capire.bookshop as my } from '../db/schema';

@cds.query.limit.default: 2 //default display number
@cds.query.limit.max: 100 //max display number

service CatalogService @(path:'/browse') {

  @readonly entity Books as SELECT from my.Books {*,
    author.name as author
  } excluding { createdBy, modifiedBy };

}
