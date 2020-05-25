using { Currency, managed, sap, cuid } from '@sap/cds/common';
namespace sap.capire.bookshop;
extend cuid  {
    extend ID  @odata.Type:'Edm.String';
}

aspect addinfo{
  title  : localized String(111);
  descr  : localized String(1111);  
  stock  : Integer;
  price  : Decimal(9,2);
  currency : Currency;  
  language : String(2);
}

entity Books : managed,addinfo,cuid {

  author : Association to Authors;
  genre  : Association to Genres;
}

entity Authors : managed, cuid {
  name   : String(111);
  dateOfBirth  : Date;
  dateOfDeath  : Date;
  placeOfBirth : String;
  placeOfDeath : String;
  books  : Association to many Books on books.author = $self;
  movies : Association to many Movies on movies.author = $self;
}

/** Hierarchically organized Code List for Genres */
entity Genres : sap.common.CodeList, cuid {
  parent   : Association to Genres;
  children : Composition of many Genres on children.parent = $self;
}

entity Movies @(cds.autoexpose) : addinfo, cuid { // if movies be associate to other entity, it will auto expose
  publisher: String(10);
  author : Association to Authors;
  genre  : Association to Genres;
}

entity Orders : cuid, managed {
  OrderNo  : String ; //> readable key
  Items    : Composition of many OrderItems on Items.parent = $self;
  total    : Decimal(9,2);
  title    : String;
  currency : Currency;
}

entity OrderItems : cuid {
  parent    : Association to Orders;
  book      : Association to Books;
  amount    : Integer;
  netAmount : Decimal(9,2);
}

annotate OrderItems with {amount @assert.range: [ 0, 3 ]}
