/*
 Copyright (C) 2018 Google Inc.
 Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
 */

import Ctrl from '../tree/tree-view';

describe('TreeView Controller', function () {
  'use strict';

  describe('{original_list} remove event handler', function () {
    let ctrlInst; // fake controller instance
    let method;
    let removeEventHandler;
    let tvClass = 'cms_controllers_tree_view_node';

    function genFilteredList(num) {
      let items = [];
      for (let i = 1; i <= num; i++) {
        items.push({
          element: $(`<tr class="${tvClass}" data-object-id="${i}"></tr>`)
            .appendTo(ctrlInst.element).get(0),
          options: new can.Map({
            instance: {
              id: i,
            },
          }),
        });
      }
      return new can.List(items);
    }

    function genList(num) {
      let items = [];
      for (let i = 1; i <= num; i++) {
        items.push({
          instance: new can.Map({
            id: i,
          }),
        });
      }
      return new can.List(items);
    }

    beforeEach(function () {
      ctrlInst = {
        element: $('<div></div>'),
        removeFromList: jasmine.createSpy('removeFromList'),
      };

      ctrlInst.options = new can.Map({
        filteredList: genFilteredList(5),
        list: genList(5),
      });

      method = Ctrl.prototype.removeFromList.bind(ctrlInst);
      removeEventHandler =
        Ctrl.prototype['{original_list} remove'].bind(ctrlInst);
    });

    it('should remove first element from both lists and its element from DOM ',
      function () {
        let removedItems = [new can.Map({id: 1})];
        let callArgs;
        let rowSelector = '.cms_controllers_tree_view_node[data-object-id="1"]';
        expect(ctrlInst.element.find(rowSelector).length).toEqual(1);

        removeEventHandler(null, {type: 'remove'}, removedItems, 0);

        callArgs = ctrlInst.removeFromList.calls.allArgs();
        expect(callArgs[0]).toEqual([ctrlInst.options.attr('list'), [1]]);
        expect(callArgs[1])
          .toEqual([ctrlInst.options.attr('filteredList'), [1]]);
        expect(ctrlInst.element.find(rowSelector).length).toEqual(0);
      });

    it('should remove first item from filteredList', function () {
      let filteredListIds;

      method(ctrlInst.options.attr('filteredList'), [1]);

      expect(ctrlInst.options.attr('filteredList').length).toBe(4);
      filteredListIds = ctrlInst.options.attr('filteredList')
        .map((item) => item.options.attr('instance.id')).serialize();
      expect(filteredListIds).toEqual([2, 3, 4, 5]);
    });

    it('should remove fist item from list', function () {
      let listIds;
      method(ctrlInst.options.attr('list'), [1]);

      expect(ctrlInst.options.attr('list').length).toBe(4);

      listIds = ctrlInst.options.attr('list')
        .map((item) => item.attr('instance.id')).serialize();
      expect(listIds).toEqual([2, 3, 4, 5]);
    });
  });
});
