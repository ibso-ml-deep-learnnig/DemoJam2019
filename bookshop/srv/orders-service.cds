using { sap.capire.bookshop as db } from '../db/schema';

service OrdersService {
  entity Orders as select from db.Orders {*} excluding { title };
  @cds.query.limit : 2 //default display 2 books
  entity Books as projection on db.Books;

  @requires_: 'authenticated-user'
  action submitOrder (book : Books.ID, amount: Integer);  

  annotate Orders with { total @mandatory };//field total is mandatory when create orders
  //annotate Orders with {modifiedAt @odata.etag};//etag is used for do the access control based on modify date
};
