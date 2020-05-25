using { sap.capire.bookshop as db } from '../db/schema';
using { cuid } from '@sap/cds/common';
service AdminService {


  entity Books as projection on db.Books;
  entity Authors as select from db.Authors {*, Authors.name as author};
  entity Orders as select from db.Orders {*} excluding { title };


  annotate Orders with { OrderNo @title:'Order Number' };
  annotate Orders with { total @readonly };//total field is readonly
  annotate Books with { author @cds.api.ignore };//ignore fields to odata api
  
}

annotate AdminService with @(requires:'admin');
