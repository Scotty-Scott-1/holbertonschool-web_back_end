export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get getCode() {
    return this._code;
  }

  set setCode(newcode) {
    this._code = newcode;
  }

  get getName() {
    return this._name;
  }

  set setName(newname) {
    this._name = newname;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
