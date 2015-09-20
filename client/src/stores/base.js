import { EventEmitter } from 'events';
import appDispatcher from '../dispatcher/app-dispatcher';

export default class BaseStore extends EventEmitter {

  constructor() {
    super();
    this._handlers = {};
    this.subscribe(() => this._registerToActions.bind(this));
  }

  _registerToActions(action) {
    if (this._handlers[action.type]) {
      this._handlers[action.type](action);
    }
  }

  _addHandler(actionType, handler) {
    this._handlers[actionType] = handler;
  }

  subscribe(actionSubscribe) {
    this._dispatchToken = appDispatcher.register(actionSubscribe());
  }

  get dispatchToken() {
    return this._dispatchToken;
  }

  emitChange() {
    this.emit('CHANGE');
  }

  addChangeListener(cb) {
    this.on('CHANGE', cb);
  }

  removeChangeListener(cb) {
    this.removeListener('CHANGE', cb);
  }
}
