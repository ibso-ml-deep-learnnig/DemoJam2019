const cds = require('@sap/cds')
module.exports = async function (){
  const db = await cds.connect.to('db') // connect to database service
  const { Books } = db.entities         // get reflected definitions

  //begin test query
  // let query = SELECT.from(Books).where({title:"Eleonora"})
  // let books = await db.run (query)
  // if (books) console.log(books[0].ID)
  //end test query
  
  // Add some discount for overstocked books
  this.after ('READ','Books', each => {
    
    const m = this.model //> this = service instance
    for (let each in this.entities) {
      const e = this.entities [each]
      console.log (`entity ${e.name} {`)
      for (let a of m.each (cds.Association, /*in:*/ e.elements))
        if (a.is2many)  console.log (`   ${a.name} : Association to many ${a._target.name};`)
      console.log (`}`)
    }
    if (each.stock > 111)  each.title += ` -- 11% discount!`
  })  
}