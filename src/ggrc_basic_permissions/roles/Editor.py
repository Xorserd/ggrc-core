# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

scope = "System"
description = """
  This role grants a user basic object creation and editing permission.
  """
permissions = {
    "read": [
        "AccessControlList",
        "Audit",
        "Snapshot",
        "Categorization",
        "Category",
        "Comment",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "Assessment",
        "AssessmentTemplate",
        "CustomAttributeDefinition",
        "CustomAttributeValue",
        "Issue",
        "DataAsset",
        "AccessGroup",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "Person",
        "Program",
        "Proposal",
        "Revision",
        "Role",
        "Context",
        "UserRole",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "create": [
        "Audit",
        "Snapshot",
        "Workflow",
        "Categorization",
        "Category",
        "Comment",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "CustomAttributeDefinition",
        "CustomAttributeValue",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "DataAsset",
        "AccessGroup",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "Program",
        "Proposal",
        "Role",
        "UserRole",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        {
            "type": "Audit",
            "terms": {
                "property_name": "archived",
                "prevent_if": True
            },
            "condition": "has_not_changed"
        },
        "Snapshot",
        "Workflow",
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "CustomAttributeDefinition",
        "CustomAttributeValue",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "DataAsset",
        "AccessGroup",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectPerson",
        "Person",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Proposal",
        "Relationship",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "Program",
        "Role",
        "UserRole",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "delete": [
        {
            "type": "Audit",
            "terms": {
                "property_name": "archived",
                "prevent_if": False
            },
            "condition": "has_changed"
        },
        "Workflow",
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "CustomAttributeDefinition",
        "CustomAttributeValue",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "DataAsset",
        "AccessGroup",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "Program",
        "Role",
        "UserRole",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ]
}
