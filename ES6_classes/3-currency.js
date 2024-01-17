export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get getCode() {
    return this._code;
  }

  get getName() {
    return this._name;
  }

  set setName(newname) {
    this._name = newname;
  }

  set setCode(newcode) {
    this._code = newcode;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
